import openai
import glob
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer


#openai.api_key = "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"
openai.api_key = "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"

model_engine = "text-davinci-002"
all_files = glob.glob(r"C:/Users/hp/PycharmProjects/bigdataProject/texts/*")
format_text = "Subject : ...\nProject owner: ....\nWinner of the contract: ... \nPrice of the contract: ...\nCompetitors : ...\noffers : ..."

#stopped in C:/Users/hp/PycharmProjects/bigdataProject/texts\décision.pdf.txt
i= 0
for file in all_files:
    i += 1
    text = open(str(file), encoding="utf8").read().lower()
    lemmatizer = WordNetLemmatizer()
    tkens = WordPunctTokenizer().tokenize(text)
    #print(tx)
    if len(tkens) > 2024:
        print("Dépasse max tokens")
        continue
    else:
        prompt = "Please extract the following informations from the following text and please make your response in format like the following example. The informations are: the subject, the project owner, the winner of the contract, the price of the contract, the other competitors and their offers respectively. Keep compititors and their offer short, don't use bid word replace it with price word in your response. The format example :" + format_text + " the text is :" + text
        try:
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
        except (ImportError, TypeError, ValueError, IOError, KeyError):
            print("issue exception!!!")
        except openai.error.RateLimitError:
            print(str(file))
            break
        else:
            message = completions.choices[0].text
            # print(message)
            if len(message) == 0:
                print("issue reading!!!")
            else:
                with open("C:/Users/hp/PycharmProjects/bigdataProject/other_textos/" + str(i) + ".txt", "w",
                          encoding="utf8") as my_output_file:
                    my_output_file.write(message)
                    my_output_file.close()
                print(i)



