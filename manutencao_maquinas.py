# ====================================================================
# PROJECT: PREDICTIVE MACHINE MAINTENANCE (INDUSTRIAL IOT CONCEPT)
# PROJETO: MANUTENÇÃO PREDITIVA DE MÁQUINAS (CONCEITO INDUSTRIAL)
# ====================================================================
# Objetivo: Monitorar horas de operação, aplicando regras de
# manutenção preventiva, crítica e alertas de folga sazonal.

print("--- SISTEMA DE MONITORAMENTO DE ATIVOS (FÁBRICA) ---")

# 1. ENTRADA DE DADOS (Simulando sensores das máquinas)
id_maquina = "PRENSA-MOTO-03"
horas_trabalhadas = 460       
epoca_sazonal_alta = True     

print(f"Analisando Equipamento: {id_maquina}")
print(f"Horômetro Atual: {horas_trabalhadas} horas")
print(f"Período de Alta Demanda Sazonal? {'SIM' if epoca_sazonal_alta else 'NÃO'}")
print("-" * 50)

# 2. PROCESSAMENTO (Estruturas Condicionais)
if horas_trabalhadas > 1000:
    print("STATUS: [CRÍTICO] Manutenção Crítica Obrigatória!")
    print("Ação: Parada programada imediata para revisão geral.")

elif horas_trabalhadas >= 500 and horas_trabalhadas <= 1000:
    print("STATUS: [ALERTA] Manutenção Preventiva Necessária.")
    print("Ação: Agendar parada técnica para troca de componentes.")

# Margem de folga baseada em período de alta demanda sazonal
elif horas_trabalhadas >= 450 and epoca_sazonal_alta:
    print("STATUS: [ATENÇÃO] Alerta de Janela de Folga Sazonal!")
    print("Motivo: Máquina próxima de 500h em período de pico de produção.")
    print("Ação: Antecipar revisão leve para evitar quebras na alta temporada.")

else:
    print("STATUS: [OK] Operação Normal.")
    print("Ação: Equipamento liberado para rodar.")

print("-" * 50)
print("--- ANÁLISE DE ATIVOS CONCLUÍDA ---")
