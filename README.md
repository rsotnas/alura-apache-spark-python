# Alura Apache Spark Python (Formação)

1. [Iniciando um projeto Spark no Google Colab](https://www.alura.com.br/artigos/iniciando-projeto-spark-no-colab)
   * Folder: starting-spark-colab
   * Help: [Using Apache Spark Docker containers to run pyspark programs using spark-submit](https://medium.com/@mehmood9501/using-apache-spark-docker-containers-to-run-pyspark-programs-using-spark-submit-afd6da480e0f)

      ```bash
      docker compose up -d
      cd ./code/starting-spark-colab
      docker cp -L main.py spark-master-1:/opt/bitnami/spark/main.py
      docker exec spark-master-1 spark-submit --master spark://172.18.0.2:7077 main.py
      ```


<br />
<br />
<br />
<br />
<br />
<br />

### Create and run virtual environment 

```bash
python -m alura-apache-spark-python
source bin/activate
pip install -r requirements.txt
```

