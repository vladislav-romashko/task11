import langid
from googletrans import Translator, LANGUAGES
import googletrans as gt


def TransLate(txt, lang):
    try:
        translator = Translator()
        translation = translator.translate(txt, dest=lang)

        detected_lang = translation.src
        confidence = 1  # Unfortunately, the library does not provide confidence score

        translated_text = translation.text

        return f"Detected(lang={detected_lang}, confidence={confidence})\n{translated_text}\n{LANGUAGES[lang.capitalize()]}"
    except Exception as e:
        return f"Translation error: {str(e)}"


def LangDetect(txt):
    try:
        detected_lang, confidence = langid.classify(txt)
        return f"Detected(lang={detected_lang}, confidence={confidence})"
    except Exception as e:
        return f"Language detection error: {str(e)}"


def CodeLang(lang):
    try:
        if lang.lower() in gt.LANGUAGES:
            return gt.LANGUAGES[lang.lower()]
        elif lang in gt.LANGUAGES.values():
            return [key for key, value in gt.LANGUAGES.items() if value == lang][0]
        else:
            return f"Language not found: {lang}"
    except Exception as e:
        return f"Error in language code detection: {str(e)}"


if __name__ == "__main__":
    txt = "доброго ранку, як себе почуваєш?"
    lang = "en"

    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang(lang))
