import pandas as pd
from deep_translator import GoogleTranslator

input_file = 'to edit.csv'
output_file = 'translated_french_canadian.csv'

df = pd.read_csv(input_file, encoding='utf-8')


def translate_text(text):
    try:
        if pd.isna(text) or text.strip() == "":
            return text
        return GoogleTranslator(source='en', target='fr').translate(text)
    except Exception as e:
        print(f"Translation error for '{text}': {e}")
        return text


columns_to_translate = ['Ecomm Product Name',
                        'Ecomm Product Description', 'Textile Identification']

# Translate
for column in columns_to_translate:
    print(f"Translating column: {column}")
    df[column] = df[column].astype(str).apply(translate_text)

df.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"✅ Translation complete. File saved to: {output_file}")
