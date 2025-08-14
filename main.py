from src.server.app import app
from src.utils import banner
from src.utils import check_info
from dotenv import load_dotenv
from src.ml_model import test_model

load_dotenv()


def run_app():
    banner()
    check_info()
    test_model("retail_store_inventory_test.csv")
    app.run(host="0.0.0.0", port=8583, debug=False)


if __name__ == "__main__":
    run_app()





