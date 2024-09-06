import logging
from flask import jsonify, request
from . import app
from . import logic
from . import limiter

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/prediction', methods=['POST'])
@limiter.limit()
def use_prediction():
    logger.info('use_prediction has been called')

    try:
        # Получаем параметр question из URL
        question = request.args.get('question')
        
        if not question or len(question.strip()) == 0:
            logger.warning('No question provided in the request')
            return jsonify({'error': 'No question provided'}), 400

        result = logic.prediction(question)
        
        # Возвращаем результат обработки
        return jsonify({'result': result})

    except Exception as e:
        logger.error(f'Error occurred: {e}')
        return jsonify({'error': 'An error occurred while processing the request'}), 500