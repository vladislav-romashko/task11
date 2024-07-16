from googletrans import Translator


def translate_text(text, src, dest):
    """
    Translate text from source language to destination language.

    Args:
        text (str): The text to translate.
        src (str): Source language code.
        dest (str): Destination language code.

    Returns:
        str: Translated text.
    """
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=src, dest=dest).text
        return translated_text
    except Exception as e:
        return f"Translation error: {str(e)}"


def detect_language(text, mode):
    """
    Detect the language of the given text.

    Args:
        text (str): The text to detect language.
        mode (str): Mode of output ('lang' or 'confidence').

    Returns:
        str: Detected language code or confidence score.
    """
    translator = Translator()
    try:
        detection = translator.detect(text)
        if mode == "lang":
            return detection.lang
        elif mode == "confidence":
            return str(detection.confidence)
        else:
            return f"Language: {detection.lang}, Confidence: {str(detection.confidence)}"
    except Exception as e:
        return f"Language detection error: {str(e)}"


def get_language_code(lang):
    """
    Get the language code for the given language.

    Args:
        lang (str): Language name.

    Returns:
        str: Language code.
    """
    translator = Translator()
    try:
        lang_code = translator.translate(lang, dest='en').src
        return lang_code
    except Exception as e:
        return f"Language code error: {str(e)}"


def list_languages(out="screen", text=None):
    """
    List all supported languages.

    Args:
        out (str): Output mode ('screen' or 'file').
        text (str): Text to translate for each language.

    Returns:
        str: Status message.
    """
    translator = Translator()
    try:
        languages = {
            'English': 'en',
            'Ukrainian': 'uk',
            'Spanish': 'es',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
        }
        if out == "screen":
            table = "N\tLanguage\t\tLanguage Code\tTranslated Text\n--------------------------------------------------------"
            for i, (lang_name, lang_code) in enumerate(languages.items(), start=1):
                lang_translation = translate_text(text, src='en', dest=lang_code) if text else ""
                table += f"\n{i}\t{lang_name}\t{lang_code}\t\t{lang_translation}"
            print(table)
            return "Ok"
        elif out == "file":
            return "Ok"
    except Exception as e:
        return f"Language list error: {str(e)}"


if __name__ == "__main__":
    list_languages(out="screen", text="Hello")
