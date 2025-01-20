import json

def lambda_handler(event, context):
    try:
        # Parse input numbers from the event
        number1 = float(event['number1'])
        number2 = float(event['number2'])
        
        # Perform addition
        result = number1 + number2
        
        # Prepare response
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'result': result,
                'message': f'Successfully added {number1} and {number2}'
            })
        }
        
    except Exception as e:
        # Error handling
        response = {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e),
                'message': 'Failed to process numbers'
            })
        }
    
    return response