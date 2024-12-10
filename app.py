from flask import Flask, request, jsonify, send_file
import hashlib
import redis
import json
from datetime import datetime

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0)


@app.route('/')
def index():
    return send_file('index.html')

@app.route('/checksum', methods=['POST'])
def calculate_checksum():
    data = request.get_json()
    input_string = data.get('input', '')
    algorithm = data.get('algorithm', 'sha256')

    # Choix de l'algorithme de hachage
    hash_functions = {
        'sha256': hashlib.sha256,
        'md5': hashlib.md5,
        'sha1': hashlib.sha1
    }

    if algorithm not in hash_functions:
        return jsonify({"error": f"Algorithme non supporté: {algorithm}"}), 400

    # Calcul du checksum
    checksum = hash_functions[algorithm](input_string.encode()).hexdigest()

    # Sauvegarde dans Redis
    entry = {
        'input': input_string,
        'checksum': checksum,
        'algorithm': algorithm,
    }
    
    redis_client.rpush('checksums', json.dumps(entry))

    return jsonify(entry)

@app.route('/checksums', methods=['GET'])
def list_checksums():
    # Récupération de tous les checksums
    checksums = [json.loads(item) for item in redis_client.lrange('checksums', 0, -1)]
    return jsonify(checksums)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)