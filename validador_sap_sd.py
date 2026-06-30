# ====================================================================
# PROJECT: AUTOMATED SALES ORDER VALIDATOR (SAP SD CONCEPT)
# PROJETO: VALIDADOR AUTOMATIZADO DE ORDEM DE VENDA (CONCEITO SAP SD)
# ====================================================================
# Objetivo: Simular a inteligência funcional da transação VA01 no SAP,
# avaliando a integridade do pedido antes do faturamento.

print("--- INICIANDO AUDITORIA DE ORDENS DE VENDA (VA01) ---")

# 1. ENTRADA DE DADOS (Simulando dados extraídos do sistema)
documento_venda = "OV-2026-001"
material = "PECA-MOTO-04"
quantidade_pedido = 8
estoque_disponivel = 15
preco_unitario = 35.00        
limite_credito_cliente = 250.00

# 2. PROCESSAMENTO (Operadores Aritméticos e Lógicos)
valor_total_pedido = quantidade_pedido * preco_unitario

# Checagem de Regras de Negócio (Retorna True ou False)
tem_estoque = quantidade_pedido <= estoque_disponivel
credito_ok = valor_total_pedido <= limite_credito_cliente

# 3. SAÍDA DE DADOS (Estruturas Condicionais e Indentação)
print(f"Analisando Documento: {documento_venda} | Material: {material}")
print(f"Valor Total do Pedido: {valor_total_pedido:.2f}")
print("-" * 50)

if tem_estoque and credito_ok:
    print("STATUS: [SUCESSO] Ordem de Venda Liberada para Faturamento!")
    print("Ação: Gerando documento de remessa automática para o centro de distribuição.")
else:
    print("STATUS: [BLOQUEADO] Validação falhou!")
    if not tem_estoque:
        print(f" -> Motivo: Estoque insuficiente. Solicitado: {quantidade_pedido} | Disponível: {estoque_disponivel}")
    if not credito_ok:
        print(f" -> Motivo: Limite de crédito excedido. Total: {valor_total_pedido:.2f} | Limite: {limite_credito_cliente:.2f}")
    print("Ação: Pedido retido para análise da gerência funcional.")

print("-" * 50)
print("--- AUDITORIA CONCLUÍDA ---")
