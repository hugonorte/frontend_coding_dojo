from flask import Flask, request, jsonify
from back_end.back_end import quickSort

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_numbers():
    data = request.get_json()
    
    if not data or 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    numbers = data['numbers']
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({'error': 'All elements must be numbers'}), 400
    
    sorted_numbers = quickSort(numbers)
    
    return jsonify({'sorted_numbers': sorted_numbers})

if __name__ == '__main__':
    app.run(debug=True)