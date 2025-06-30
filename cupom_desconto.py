print("=== Loja Online ===")
preco = float(input("Digite o preço do produto: "))

print("\nEscolha um cupom de desconto:")
print("[1] DESCONTO10 (10%)")
print("[2] DESCONTO20 (20%)")
print("[3] SEM_DESCONTO (0%)")
opcao = input("Digite o código do cupom: ").strip()

if opcao == "DESCONTO10" or opcao == "1":
    preco_final = preco * 0.90
elif opcao == "DESCONTO20" or opcao == "2":
    preco_final = preco * 0.80
elif opcao == "SEM_DESCONTO" or opcao == "3":
    preco_final = preco
else:
    preco_final = preco  # Caso o cupom seja inválido, sem desconto

print(f"\nPreço final: {preco_final:.2f}")