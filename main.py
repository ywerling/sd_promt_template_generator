# Prompt generator for Generative AI image filling a template with multiple variations
import csv

INPUT_TEMPLATE = 'assets/template.txt'
INPUT_PARAMETERS = 'assets/parameters.csv'
OUTPUT_FILE = 'outputs/prompts.txt'

with open(INPUT_TEMPLATE, mode ='r') as template_file:
    template_text = template_file.read()

# print(template_text)

param_list = []
with open(INPUT_PARAMETERS, mode ='r') as param_file:
  param_csv = csv.reader(param_file)
  for line in param_csv:
      param_list.append(line)
      # print(line)

# print (len(param_list))

# format param_list[row][column]
# print(param_list[0][1])

# text_to_replace = '{{'+param_list[0][0]+'}}'
# test_string = template_text.replace(text_to_replace,param_list[0][1])
# text_to_replace = '{{'+param_list[1][0]+'}}'
# test_string = test_string.replace(text_to_replace,param_list[1][2])
# print(test_string)

# for i in range(1,len(param_list[0])):
#     for j in range(1,len(param_list[1])):
#         text_to_replace = '{{' + param_list[0][0] + '}}'
#         test_string = template_text.replace(text_to_replace, param_list[i][j])
#         print(test_string)

output_lines=[]
for i in range(1,len(param_list[0])):
    text_to_replace = '{{' + param_list[0][0] + '}}'
    test_string = template_text.replace(text_to_replace, param_list[0][i])
    for j in range(1, len(param_list[1])):
        text_to_replace = '{{' + param_list[1][0] + '}}'
        test_string2 = test_string.replace(text_to_replace, param_list[1][j])
        print(test_string2)
        output_lines.append(test_string2)

with open(OUTPUT_FILE, "w", encoding='utf-8') as output_file:
    for line in output_lines:
        if len(line) > 0:
            output_file.write(line)
            output_file.write('\n')












