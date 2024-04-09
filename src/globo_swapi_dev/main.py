from src.globo_swapi_dev.transformation.run_process_pipeline import run_process_silver, run_process_bronze, \
    run_process_gold


def main(args):
    if args == 'STARWARS_BRONZE':
        run_process_bronze()
    elif args == 'STARWARS_SILVER_AND_DATABASE':
        run_process_silver()
    elif args == 'STARWARS_GOLD_AND_DATABASE':
        run_process_gold()
    else:
        print("Opção inválida")


if __name__ == "__main__":
    option = input("Escolha uma opção: ")
    main(option)
