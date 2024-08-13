import random

def generate_card_number(currency: str, client_id: int) -> str:
    if currency == "FCFA":
        prefix = "241"
    elif currency == "MAD":
        prefix = "212"
    else:
        raise ValueError("Devise non supportée. Utilisez 'FCFA' ou 'MAD'.")

    # Convertir l'ID du client en chaîne de caractères
    client_id_str = str(client_id)
    
    # Calculer le nombre de chiffres aléatoires nécessaires pour compléter les 16 chiffres
    num_random_digits = 16 - len(prefix) - len(client_id_str)
    
    # Générer des chiffres aléatoires pour compléter le numéro
    random_digits = ''.join(random.choices("0123456789", k=num_random_digits))
    
    # Combiner le préfixe, l'ID du client, et les chiffres aléatoires pour former le numéro de carte complet
    card_number = prefix + client_id_str + random_digits
    
    return card_number

# Exemple d'utilisation
currency = "FCFA"
client_id = 100
card_number = generate_card_number(currency, client_id)
print("Numéro de carte généré:", card_number)

currency = "MAD"
client_id = 200
card_number = generate_card_number(currency, client_id)
print("Numéro de carte généré:", card_number)
