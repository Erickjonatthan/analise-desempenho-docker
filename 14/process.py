import time
import random

print("Iniciando processamento de dados...")

# Simula processamento de dados
for i in range(5):
    print(f"Processando batch {i+1}/5...")
    # Simula tempo de processamento
    time.sleep(random.uniform(0.5, 2.0))
    
    # Simula algum cálculo
    data_size = random.randint(1000, 5000)
    processed = data_size * 0.85
    print(f"  - Processados {processed:.0f} registros de {data_size}")

print("Processamento concluído com sucesso!")