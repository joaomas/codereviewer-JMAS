
from src.Validator import Validator
import xml.etree.ElementTree as ET



class Validator_XML(Validator):
    """_summary_
    XML structure Validator for RuleValidator_XML rules
    """


    def __init__(self, parser_xml_in) -> None:
        super().__init__()
        self.parser_xml = parser_xml_in  #scturcture xml


    # TODO - pass a file or directory ?
    def run_validator(self, file_f90):

        xml = self.parser_xml.parse(file_f90)
        str_errors=''

        # code from QA

        # OK -------
        # test rule verify_file_ext
        ## read the files and get fields
        # tree = ET.parse('../xml/saida.xml')
        # root = tree.getroot() # Pega a raiz do xml

        xml_struct = ET.ElementTree(xml)
        root = xml_struct.getroot()



        for file in root.iter("file"): #Pega o nome e caminho do arquivo fonte
            full_file_name = file.get("path")

        rule_verify_file_ext = self.rule_validator_dic['verify_file_ext']

        list_names = full_file_name.split("/")
        file_name  = list_names[-1]
        print("file_name: ", file_name)

        str_errors += rule_verify_file_ext.check(file_name)
        # # Test rule implicit none
        # Abre e lê o arquivo fonte

        fn = open(full_file_name, "r")
        lines        = fn.readlines()
        lines_work   = []
        c_lines_work = []

        comments = {}


        # comments = search_comments(root)
        # #print(comments)
        # # Percorre as linhas de entrada e reescreve retirando os comentários
        # for line in range(len(lines)):
        #     try:
        #         ndx = comments.get("line").index(line)
        #     except:
        #         lines_work.append(lines[line])
        #         continue
        #     lines_work.append(lines[line][0:comments.get("col_begin")[ndx]])

        # c_comments = {}
        # c_line = []
        # c_begin = []
        # c_end = []

        # # Cria um dicionário com a posição de Literais char
        # for clc in root.iter("char-literal-constant"):
        #     c_line.append(int(clc.get("line_begin"))-1)
        #     c_begin.append(int(clc.get("col_begin")))
        #     c_end.append(int(clc.get("col_end")))
        # c_comments.update({"line":c_line, "col_begin":c_begin, "col_end":c_end})

        # # Percorre as linhas de line_work e reescreve em c_line_work retirando os literais char
        # for line in range(len(lines_work)):
        #     try:
        #         ndx = c_comments.get("line").index(line)
        #     except:
        #         c_lines_work.append(lines_work[line])
        #         continue
        #     # Copia a parte que está fora dos literais
        #     new_line = lines_work[line][0:c_comments.get("col_begin")[ndx] + 1] \
        #                 + lines_work[line][c_comments.get("col_end")[ndx]-1:]
        #     c_lines_work.append(new_line)

        # # Cria um dicionário com as linhas de atribuição
        # assignments = {}
        # a_line = []
        # a_begin = []
        # a_end = []

        # # Cria uma lista com todas as linhas que tem atribuição
        # for assig in root.iter("assignment"):
        #     a_line.append(int(assig.get("line_begin")))
        #     a_begin.append(int(assig.get("col_begin")))
        #     a_end.append(int(assig.get("col_end")))
        # assignments.update({"line":a_line, "col_begin":a_begin, "col_end":a_end})

        # # Tabela de palavras reservadas
        # keywords = [ "abstract", "allocatable", "allocate", "assign", "associate",
        #                 "asynchronous", "backspace, bind", "block", "block data",
        #                 "call", "case", "class", "close", "codimension", "common",
        #                 "concurrent","contains", "contiguous", "continue", "critical",
        #                 "cycle", "data", "deallocate", "deferred", "dimension", "do",
        #                 "elemental", "else", "elseif", "elsewhere", "end","endif",
        #                 "end do", "endfile", "end if", "end module",
        #                 "end select", "end subroutine", "entry", "enum", "enumerator",
        #                 "equivalence", "error", "exit", "extends", "external", "final",
        #                 "flush", "forall", "format", "function", "generic", "goto",
        #                 "if", "implicit", "import", "include", "inquire", "intent",
        #                 "interface", "intrinsic", "lock", "memory", "module", "namelist",
        #                 "non_overridable", "nopass", "nullify", "only", "open",
        #                 "operator", "optional", "parameter", "pass", "pause", "pointer",
        #                 "print", "private", "procedure", "program", "protected",
        #                 "public", "pure", "read", "recursive", "result", "return", "rewind",
        #                 "rewrite", "save", "select", "sequence", "stop", "submodule",
        #                 "subroutine", "sync", "sync all", "sync images", "target", "then",
        #                 "unlock", "use", "value", "volatile", "wait", "where", "while",
        #                 "write" ]

        # # Tabelas de palavras reservadas não-aceitas
        # not_keywords = [ "enddo", "endif", "goto", "pause", "equivalence","common",
        #                 "save", "data", "double precision","stop" ]

        # # Inicio do processo com a análise das subrotinas
        # # Percorre a árvore para as declarações de subrotina
        # points = 0.0



        # TODO Create Rule
        # points = verify_module_name(points, full_file_name, root)
        rule_verify_module_name = self.rule_validator_dic['verify_module_name']
        str_errors += rule_verify_module_name.check(file_name)



        # for sub in root.iter("subroutine"):
        #     print("\n\nInspecionando a subrotina", sub.get("name"))
        #     print("---------------------------------------------------------")
        #     print("subroutine lines = ", int(sub.get("line_end")) - int(sub.get("line_begin")))
        #     print("---------------------------------------------------------")

        #     points = 0.0
        #     p_proc_name = FALSE
        #     p_src_name = FALSE
        #     name_list= search_namelist(sub)
        #     used_keywords = search_keywords(sub, keywords)

        #     # #eval() #execução a partir de strings

        #     # for key, value1 in dict.getitem()
        #     #    eval

        #     points = case_keywords(sub, keywords, points)
        for sub in root.iter("subroutine"):
           print("\n\nInspecionando a subrotina", sub.get("name"))
#       print("---------------------------------------------------------")
#       print("subroutine lines = ", int(sub.get("line_end")) - int(sub.get("line_begin")))
#       print("---------------------------------------------------------")

#       points = 0.0
#       p_proc_name = FALSE
#       p_src_name = FALSE
#       name_list= search_namelist(sub)
#       used_keywords = search_keywords(sub, keywords)

#       # #eval() #execução a partir de strings

#       # for key, value1 in dict.getitem()
#       #    eval

#       points = case_keywords(sub, keywords, points)
#       points = verify_name_list(points, name_list)
#       points = case_keyword_variables(sub, points, keywords,\
#                                       not_keywords, name_list["id"])
#       points = keywords_in_line(sub, keywords, points)
#       points = verify_col_end(sub, points)
#       points = verify_colapsed_keywords(points,used_keywords)

#       points = verify_deallocate(sub, points)

#       print("Dealloacate ---->")
# #      points = verify_deallocate(sub,points)
#       points = verify_allocate(sub,points)
#       print("Fim Dealloacate ---->")

#       # Verifica a primeira Rule de nome
#       if not is_camel_case(sub.get("name")): #4.8 camelCase
#          print("Rule 4.8 : camelCase : lines", \
#                 sub.get("line_begin"), sub.get("line_end"))
#          points = points + 1.0

#       arguments = []
#       intent_list = []
#       # Inspeciona o header da subrotina
      #  for elem in sub.iter("header"):
      #    # Inspeciona os argumentos de chamada
      #    for args in elem.iter("arguments"):
      #       # Inspeciona o nome dos argumentos dentro das Rules
      #       for arg in args.iter("argument"):
      #          if type(arg.get("name")) != str: #Previne da leitura de não strings
      #             continue

      #          # Preenche a lista de argumentos de chamada da subrotina
      #          arguments.append(arg.get("name"))

      #          # Verifica a Rule de nome de variável e a Rule de nomes curtos
      #          if not is_snake_case(arg.get("name")): #4.7 snake_case
      #             print("Rule 4.7 : snake_case : line", \
      #                    arg.get("line_begin"), arg.get("name"))
      #             points = points + 1.0
      #          if arg.get("name") in keywords:
      #             print("Rule 4.71 : keyword : line",\
      #                    arg.get("line_begin"), arg.get("name"))
      #             points = points + 1.0
      #          if arg.get("name") in not_keywords:
      #             print("Rule 4.71 : not_keyword : line",\
      #                    arg.get("line_begin"), arg.get("name"))
      #             points = points + 1.0

      # # Inspeciona o corpo da subrotina
      #  has_implicit = False
      #  has_use = False
      #  has_only = False
           for elem in sub.iter("body"):
         ##### Falta olhar os comentários
                for spc in elem.iter("specification"):
                   for dec in spc.iter("declaration"):

                  # Verificação da declaração de implicit
                  # for ist in dec.iter("implicit-stmt"):
                  #    has_implicit = True #Informa que a declaração de implicit foi encontrada
                  #    # Verifica a Rule de implicit none obrigatório
                  #    if not ist.get("implicitKeyword") == "implicit" \
                  #       and not ist.get("noneKeyword") == "none": #4.28- sem implicit
                  #       print("Rule 4.28 : no implicit : lines", \
                  #              spc.get("line_begin"), spc.get("line_end"))
                  #       points = points + 0.5

                   # # Verifica quais linhas com delacaração de parameter
                   # # Guarda na lista lines_with_parameter

                       lines_with_parameter = []
                       for atp in dec.iter("attribute-parameter"):
                           lines_with_parameter.append(atp.get("line_begin"))
               #    #atp.get("line_begin")) + 1  # linha seguinte ao parametro
               #    if (int(atp.get("line_begin")) -1)  not in comments.get("line"):
               #       print("Rule 4.11.2/12.2 : commnents line:",\
               #              int(atp.get("line_begin")) - 1)
               #       points = points + 1.0
               #    #---->verificar regras
               #    elif "!!" not in comments.get("txt_comment")[comments.get("line").index(int(atp.get("line_begin")) + 1) ]:
               #       print("Rule 4.11.2/12.2 : commnents line (!!) :",\
               #              int(atp.get("line_begin") + 1) )
               #       points = points + 1.0
               #    elif len(comments.get("txt_comment")[comments.get("line").index(int(atp.get("line_begin")) + 1) ].strip())  <= 2:
               #       print("Rule 4.11.2/12.2 : small commnents :",\
               #              int(atp.get("line_begin")) + 1)
               #       points = points + 1.0

               # for itt in dec.iter("intent"):
               #    intent = itt.get("type")
               #    itt_line_begin = itt.get("line_begin")
               #    itt_line_end = itt.get("line_end")
               #    intent_list.append(itt_line_begin)

               # p_proc_name = FALSE
               # p_srcc_name = FALSE
                       for vars in dec.iter("variables"):
                          for var in vars.iter("variable"):
                             if type(var.get("name")) != str: #Previne da leitura de não strings
                                continue
                     # Dados da variável: nome, linha
                             var_name = var.get("name")
                             line_begin = var.get("line_begin")
                             line_end = var.get("line_end")

                         #print("variable: ", var_name)
                             rule_verify_snake_case = self.rule_validator_dic["verify_snake_case"]
                             str_errors += rule_verify_snake_case.check(var_name)


                        # word =
                        # rule_snake = self.rule_validator_dic['snake_case']
                        # str_checks =  rule_snake.check(word)


        # # Test rule implicit none
        #
        #

        return str_errors
