from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs


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
    try:
        translated_text = GoogleTranslator(source=src, target=dest).translate(text)
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
    try:
        detection = detect_langs(text)
        if mode == "lang":
            return detection[0].lang
        elif mode == "confidence":
            return str(detection[0].prob)
        else:
            return f"Language: {detection[0].lang}, Confidence: {str(detection[0].prob)}"
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
    try:
        lang_code = GoogleTranslator(target='en').translate(lang, source='en')
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
    try:
        languages = GoogleTranslator(source='en', target='en').get_supported_languages()
        if out == "screen":
            table = "Language Code\tLanguage Name\t\tTranslated Text\n--------------------------------------------------------"
            for i, lang in enumerate(languages, start=1):
                lang_code = get_language_code(lang)
                translation = translate_text(text, src='en', dest=lang) if text else ""
                table += f"\n{i}\t{lang}\t{lang_code}\t{translation}"
            print(table)
            return "Ok"
        elif out == "file":
            return "Ok"
    except Exception as e:
        return f"Language list error: {str(e)}"


if __name__ == "__main__":
    list_languages(out="screen", text="Hello")

