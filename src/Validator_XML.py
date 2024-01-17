
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
        
        # Abre e lê o arquivo fonte
        fn = open(full_file_name, "r")
        lines = fn.readlines()
        lines_work = []
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
        # points = verify_module_name(points, full_file_name, root)

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


        
        
            
        # subroutines
        # Test rule camel case
        
        # TODO
        # word = 'TODO from xml'
        # rule_snake = self.rule_validator_dic['snake_case']


        # str_checks =  rule_snake.check(word)
        # # Test rule implicit none 
        #
        #   
        
        
        
            
        return str_errors
        
        

        
        
        
