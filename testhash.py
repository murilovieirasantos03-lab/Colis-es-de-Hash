def calcula_hash(palavra):
    return sum(ord(letra) for letra in palavra)

def rodar_desafio():
    print("=== TESTADOR DE COLISÃO DE HASH ===")
    print("Digite 'sair' a qualquer momento para fechar o programa.\n")
    
    while True:
        p1 = input("Digite a primeira palavra: ").strip()
        if p1.lower() == 'sair':
            break
            
        p2 = input("Digite a segunda palavra: ").strip()
        if p2.lower() == 'sair':
            break
        
        # Validação mínima
        if len(p1) < 2 or len(p2) < 2:
            print("\n⚠️  Erro: Ambas as palavras devem ter pelo menos 2 letras.\n")
            continue
            
        hash1 = calcula_hash(p1)
        hash2 = calcula_hash(p2)
        
        print(f"\n--- Resultado ---")
        print(f"Palavra 1 ('{p1}'): {hash1}")
        print(f"Palavra 2 ('{p2}'): {hash2}")
        
        if p1 == p2:
            print("⚠️  Você digitou a mesma palavra! Tente palavras diferentes.")
        elif hash1 == hash2:
            print("🎯 BOOA! Você encontrou uma colisão! Duas palavras diferentes com o mesmo hash.")
        else:
            print("❌ Não foi desta vez. Os hashes deram diferentes.")
            
        print("-" * 30 + "\n")

if __name__ == "__main__":
    rodar_desafio()