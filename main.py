# from src.server.app import app
# from src.utils import banner
# from src.utils import check_info



# def run_app():
#     banner()
#     check_info()
#     app.run(host="0.0.0.0", port=8583, debug=False)


# if __name__ == "__main__":
#     run_app()


from src.ml_model import train_model


train_model("retail_store_inventory_test.csv", "retail_store_inventory_train.csv")