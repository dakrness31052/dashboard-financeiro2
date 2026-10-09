import pandas as pd

# Dados financeiros consolidados por sede e mês (2026)
data_sedes = [
    # Maio
    {"Mês": "Maio", "Sede": "Água Verde", "Faturamento": 137568.30, "Gasto Fixo": 75677.61, "Gasto Variável": 44209.41},
    {"Mês": "Maio", "Sede": "Portão", "Faturamento": 127257.08, "Gasto Fixo": 70143.32, "Gasto Variável": 43628.13},
    {"Mês": "Maio", "Sede": "Sede 01 (Praia)", "Faturamento": 10217.25, "Gasto Fixo": 7926.19, "Gasto Variável": 0.0},
    # Junho
    {"Mês": "Junho", "Sede": "Água Verde", "Faturamento": 147369.33, "Gasto Fixo": 68500.00, "Gasto Variável": 44100.00},
    {"Mês": "Junho", "Sede": "Portão", "Faturamento": 139771.35, "Gasto Fixo": 62581.66, "Gasto Variável": 47710.65},
    {"Mês": "Junho", "Sede": "Sede 01 (Praia)", "Faturamento": 10217.25, "Gasto Fixo": 8038.62, "Gasto Variável": 0.0},
    # Julho
    {"Mês": "Julho", "Sede": "Água Verde", "Faturamento": 147369.33, "Gasto Fixo": 101760.48, "Gasto Variável": 43837.75},
    {"Mês": "Julho", "Sede": "Portão", "Faturamento": 139771.35, "Gasto Fixo": 69100.00, "Gasto Variável": 49906.12},
    {"Mês": "Julho", "Sede": "Sede 01 (Praia)", "Faturamento": 10217.25, "Gasto Fixo": 8038.62, "Gasto Variável": 0.0},
    # Agosto
    {"Mês": "Agosto", "Sede": "Água Verde", "Faturamento": 147672.50, "Gasto Fixo": 67403.49, "Gasto Variável": 52939.34},
    {"Mês": "Agosto", "Sede": "Portão", "Faturamento": 140131.02, "Gasto Fixo": 80714.38, "Gasto Variável": 55769.44},
    {"Mês": "Agosto", "Sede": "Sede 01 (Praia)", "Faturamento": 10217.25, "Gasto Fixo": 8035.33, "Gasto Variável": 0.0},
]

# Painel de despesas dos sócios
data_socios = [
    {"Mês": "Maio", "Marlon": 25170.09, "Dani": 28246.72, "Total Sócios": 53416.81},
    {"Mês": "Junho", "Marlon": 28000.00, "Dani": 30716.86, "Total Sócios": 58716.86},
    {"Mês": "Julho", "Marlon": 31760.85, "Dani": 33955.86, "Total Sócios": 65716.71},
    {"Mês": "Agosto", "Marlon": 36487.19, "Dani": 33861.51, "Total Sócios": 70348.70},
]

df_sedes = pd.DataFrame(data_sedes)
df_sedes["Despesa Total Sede"] = df_sedes["Gasto Fixo"] + df_sedes["Gasto Variável"]
df_sedes["Resultado Sede"] = df_sedes["Faturamento"] - df_sedes["Despesa Total Sede"]

df_socios = pd.DataFrame(data_socios)

print("=== DEMONSTRATIVO POR SEDE ===")
print(df_sedes.to_string(index=False))

print("\n=== DESPESAS DOS SÓCIOS ===")
print(df_socios.to_string(index=False))