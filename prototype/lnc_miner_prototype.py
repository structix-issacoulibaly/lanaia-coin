==============================================
LNC MINER PROTOTYPE V0.1
==============================================
PROTOTYPE DE SIMULATION
SIMULE LA LOGIQUE D'EMISSION LNC
CE CODE NE MINE PAS DE VRAIS LNC
==============================================

BLOCS_PAR_ERE = 1_050_000
RECOMPENSE_INITIALE = 10.0
TEMPS_BLOC_SEC = 120

def get_recompense(hauteur_bloc):
    """Calcule la récompense de bloc en fonction de la hauteur"""
    era = hauteur_bloc // BLOCS_PAR_ERE
    reward = RECOMPENSE_INITIALE / (2 ** era)
    return reward

def get_annee(hauteur_bloc):
    """Convertit la hauteur de bloc en années approximatives"""
    secondes = hauteur_bloc * TEMPS_BLOC_SEC
    annees = secondes / (60 * 60 * 24 * 365)
    return annees

def simuler_emission():
    print("==============================================")
    print("     SIMULATEUR LANAIA COIN - LNC V0.1")
    print("==============================================")
    print(f"Offre Cible Maximale: 21,000,000 LNC")
    print(f"Halving: tous les {BLOCS_PAR_ERE:,} blocs ~4 ans")
    print(f"Temps de bloc: {TEMPS_BLOC_SEC} secondes\n")
    
    cumul = 0.0
    print(f"{'Ère':<4} | {'Année':<8} | {'Récompense':<12} | {'Émission Ère':<15} | {'Cumul':<15}")
    print("-"*85)
    
    for i in range(0, 8):
        bloc_debut = i * BLOCS_PAR_ERE
        reward = get_recompense(bloc_debut)
        emission_ere = reward * BLOCS_PAR_ERE
        cumul += emission_ere
        annee = get_annee(bloc_debut)
        
        print(f"{i:<4} | {annee:<8.1f} | {reward:<12.8f} | {emission_ere:<15,.0f} | {cumul:<15,.0f}")

    print("-"*85)
    print(f"\nNote: Le cumul tend asymptotiquement vers 21,000,000 LNC")
    print(f"      L'unité minimale et l'arrondi final seront définis en V2")

if __name__ == "__main__":
    simuler_emission()
