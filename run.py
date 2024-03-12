from api import create_app, create_db
import os
from pathlib import Path

if __name__ == '__main__':
    app = create_app()
    if not os.path.exists(Path('instance', 'database.db')):
        create_db()
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True, host='0.0.0.0', port=5000)
