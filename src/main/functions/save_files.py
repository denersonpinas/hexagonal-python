import os
import uuid
from werkzeug.utils import secure_filename
from src.constants.reference import UPLOAD_FOLDER
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpResponse


def saved_files(files):

    try:
        for chave, file in dict(files).items():
            name = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
            savePath = os.path.join(UPLOAD_FOLDER, name)
            file.save(savePath)

    except Exception as exc:  # noqa: E722
        print("Error encontrado: ", exc)
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return HttpResponse(status_code=201, body={"message": "OK!"})
