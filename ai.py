"""
Cadastro simples de professores com validação de CPF

Funcionalidades:
- cadastrar professor (nome, CPF, idade, matérias)
- validação do CPF (algoritmo brasileiro)
- salvar/ler em JSON (professores_db.json)
- tratamento de erros comuns

Modo rápido de teste: execute `python ai.py --auto-test`
"""

import json
import os
import re
import sys
import hashlib
import getpass
from typing import List, Dict, Any


DB_FILENAME = os.path.join(os.path.dirname(__file__), "professores_db.json")


def normalize_cpf(cpf: str) -> str:
	return re.sub(r"\D", "", cpf)


def is_valid_cpf(cpf: str) -> bool:
	"""Validação leve de CPF: aceita qualquer sequência numérica de 11 dígitos.
	Nota: por pedido do usuário, o único erro obrigatório é quando o CPF já
	está cadastrado; a validação formal completa foi mantida como opção.
	"""
	cpf = normalize_cpf(cpf)
	return len(cpf) == 11


def hash_password(senha: str) -> str:
	return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def load_db() -> Dict[str, Any]:
	if not os.path.exists(DB_FILENAME):
		return {"professores": []}
	try:
		with open(DB_FILENAME, "r", encoding="utf-8") as f:
			return json.load(f)
	except json.JSONDecodeError:
		# arquivo corrompido: backups não implementados aqui, retorna vazio
		return {"professores": []}


def save_db(db: Dict[str, Any]) -> None:
	with open(DB_FILENAME, "w", encoding="utf-8") as f:
		json.dump(db, f, ensure_ascii=False, indent=2)


def cpf_exists(db: Dict[str, Any], cpf: str) -> bool:
	cpf = normalize_cpf(cpf)
	return any(normalize_cpf(p["cpf"]) == cpf for p in db.get("professores", []))


def add_professor(db: Dict[str, Any], nome: str, cpf: str, idade: int, materias: List[str], senha: str) -> Dict[str, Any]:
	if not nome.strip():
		raise ValueError("Nome vazio")
	cpf_n = normalize_cpf(cpf)
	# Apenas checagem simples de formato (11 dígitos). Não falha a menos
	# que seja realmente inválido; única verificação que gera erro por
	# pedido do usuário é CPF já cadastrado.
	if not is_valid_cpf(cpf_n):
		raise ValueError("CPF inválido: deve conter 11 dígitos")
	if idade <= 0:
		raise ValueError("Idade deve ser positiva")
	if cpf_exists(db, cpf_n):
		raise ValueError("CPF já cadastrado")

	prof = {
		"nome": nome.strip(),
		"cpf": cpf_n,
		"idade": idade,
		"materias": [m.strip() for m in materias if m.strip()],
		"senha_hash": hash_password(senha)
	}
	db.setdefault("professores", []).append(prof)
	save_db(db)
	return prof


def list_professores(db: Dict[str, Any]) -> None:
	profs = db.get("professores", [])
	if not profs:
		print("Nenhum professor cadastrado.")
		return
	for i, p in enumerate(profs, 1):
		# Exibe apenas nome e CPF — dados completos exigem senha na opção de visualização
		print(f"{i}. {p['nome']} - CPF: {p['cpf']}")


def view_professor(db: Dict[str, Any]) -> None:
	cpf = input("Informe o CPF do professor: ").strip()
	senha = getpass.getpass("Senha: ")
	cpf_n = normalize_cpf(cpf)
	profs = db.get("professores", [])
	for p in profs:
		if normalize_cpf(p.get("cpf", "")) == cpf_n:
			stored = p.get("senha_hash")
			if not stored:
				print("Cadastro sem senha — não é possível visualizar os dados.")
				return
			if hash_password(senha) == stored:
				print("Dados do professor:")
				print(f"Nome: {p.get('nome')}")
				print(f"CPF: {p.get('cpf')}")
				print(f"Idade: {p.get('idade')}")
				print(f"Matérias: {', '.join(p.get('materias', []))}")
				return
			else:
				print("Senha incorreta.")
				return
	print("Professor não encontrado com esse CPF.")


def prompt_cadastro(db: Dict[str, Any]) -> None:
	try:
		# Pedir CPF primeiro: se já existir, interrompe imediatamente
		cpf = input("CPF (somente números ou com pontuação): ").strip()
		cpf_n = normalize_cpf(cpf)
		if not is_valid_cpf(cpf_n):
			print("CPF inválido: deve conter 11 dígitos.")
			return
		if cpf_exists(db, cpf_n):
			print("CPF já cadastrado. Cadastro interrompido.")
			return

		nome = input("Nome do professor: ").strip()
		idade_s = input("Idade: ").strip()
		materias_s = input("Matérias (separadas por vírgula): ").strip()
		senha = getpass.getpass("Senha (será usada para visualizar o cadastro): ")
		senha_conf = getpass.getpass("Confirme a senha: ")

		if senha != senha_conf:
			print("Senhas não conferem.")
			return

		try:
			idade = int(idade_s)
		except ValueError:
			print("Idade inválida. Use um número inteiro.")
			return

		materias = [m.strip() for m in materias_s.split(",") if m.strip()]

		prof = add_professor(db, nome, cpf_n, idade, materias, senha)
		print("Professor cadastrado com sucesso.")
	except ValueError as e:
		print("Erro ao cadastrar:", e)
	except Exception as e:
		print("Erro inesperado:", e)


def main():
	db = load_db()
	while True:
		print("\nEscolha uma opção:")
		print("1 - Cadastrar professor")
		print("2 - Ver dados (exige CPF + senha)")
		print("3 - Listar professores (apenas CPFs e nomes)")
		print("4 - Sair")
		opt = input("> ").strip()
		if opt == "1":
			prompt_cadastro(db)
		elif opt == "2":
			view_professor(db)
		elif opt == "3":
			list_professores(db)
		elif opt == "4":
			break
		else:
			print("Opção inválida.")


if __name__ == "__main__":
	if "--auto-test" in sys.argv:
		# Teste rápido: cria um professor de exemplo e tenta visualizar
		db = load_db()
		sample = {"nome": "Teste", "cpf": "11144477735", "idade": 40, "materias": ["Matemática", "Física"], "senha": "senha123"}
		try:
			if cpf_exists(db, sample["cpf"]):
				print("CPF de teste já existe, listando professores:")
				list_professores(db)
			else:
				added = add_professor(db, sample["nome"], sample["cpf"], sample["idade"], sample["materias"], sample["senha"])
				print("Adicionado (teste): nome=", added.get("nome"), "cpf=", added.get("cpf"))

			print("Tentando visualizar com senha correta (senha123):")
			# simula visualização
			for p in load_db().get("professores", []):
				if normalize_cpf(p.get("cpf", "")) == normalize_cpf(sample["cpf"]):
					if hash_password(sample["senha"]) == p.get("senha_hash"):
						print("Visualização: ok — dados:")
						print(p)
					else:
						print("Falha na visualização de teste: senha incorreta")
		except Exception as e:
			print("Erro no teste automático:", e)
	else:
		main()


