from src.globo_swapi_dev.transformation.run_process_pipeline import run_process_silver, run_process_bronze

def main(args):
    if args == 'STARWARS_BRONZE':
        run_process_bronze()
    elif args == 'STARWARS_SILVER_AND_EXADATA':
        run_process_silver()
    else:
        print("Opção inválida")

if __name__ == "__main__":
    option = input("Escolha uma opção: ")
    main(option)