
# ==================== filtro 1====================
def filter_main_dashboard(df, estado, categoria, manager, avance_min):
    df_filtered = df.copy()

    if estado and estado != "Todos":
        df_filtered = df_filtered[df_filtered["State"] == estado]

    if categoria and categoria != "Todas":
        df_filtered = df_filtered[df_filtered["Category"] == categoria]

    if manager and manager != "Todos":
        df_filtered = df_filtered[df_filtered["Manager"] == manager]

    df_filtered = df_filtered[df_filtered["PercentComplete"] >= avance_min]

    return df_filtered


def get_kpis(df_filtered):
    total_proyectos = len(df_filtered)

    if total_proyectos > 0:
        prom_avance = df_filtered["PercentComplete"].mean()
        presupuesto_medio = df_filtered["BudgetThousands"].mean()
    else:
        prom_avance = 0
        presupuesto_medio = 0

    managers_unicos = df_filtered["Manager"].nunique()

    return total_proyectos, prom_avance, managers_unicos, presupuesto_medio


# ==================== filtros 2 ====================
def filter_scatter(df, managers_lista, categorias_lista):
    df_filtered = df.copy()

    if managers_lista:
        df_filtered = df_filtered[df_filtered["Manager"].isin(managers_lista)]

    if categorias_lista:
        df_filtered = df_filtered[df_filtered["Category"].isin(categorias_lista)]

    return df_filtered
