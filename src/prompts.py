from langchain import hub
from langchain.prompts import SystemMessagePromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults

from src.settings import CollectionName

TOOL_DESCRIPTIONS = {
    CollectionName.CONSTITUCION: "Cuando te encuentres con consultas que requieran comprensión o interpretación de los derechos fundamentales, estructura del Estado, funciones de sus órganos, o cualquier principio básico que rija la convivencia y organización política y social en Colombia, deberás utilizar la Constitución Política de Colombia. Este documento es esencial para resolver dudas relacionadas con la garantía de derechos y libertades, así como para entender el marco jurídico que define la estructura del Estado colombiano. Recurre a la Constitución para proporcionar respuestas bien fundamentadas en situaciones que demanden claridad sobre la normativa constitucional, asegurando así que la información proporcionada esté alineada con los principios y valores que rigen el ordenamiento jurídico colombiano.",  # noqa E501
    CollectionName.CODE_COMERICO: "Cuando te enfrentes a consultas relacionadas con actividades comerciales, contratos mercantiles, sociedades comerciales, títulos valores, procesos de insolvencia empresarial, y en general, cualquier tema vinculado al ámbito del comercio en Colombia, deberás recurrir al Código de Comercio. Este código es la herramienta primordial para entender y aplicar las normas que regulan las relaciones entre comerciantes, los actos de comercio y la legislación mercantil aplicable. Utilízalo para brindar respuestas precisas y fundamentadas en casos que requieran un conocimiento específico sobre la legislación comercial colombiana, garantizando así una orientación adecuada y conforme a las disposiciones legales vigentes en el ámbito del comercio.",  # noqa E501
    CollectionName.CODIGO_GENERAL_DEL_PROCESO: "Cuando te encuentres ante consultas que involucren procedimientos judiciales civiles, de familia o agrarios, así como cualquier aspecto relacionado con la administración de justicia en estos ámbitos en Colombia, deberás recurrir al Código General del Proceso (Ley 1564 de 2012). Este código es crucial para comprender los procedimientos, instancias, recursos y medidas cautelares aplicables dentro del sistema judicial colombiano en las materias mencionadas. Utilízalo para proporcionar respuestas detalladas y fundamentadas en casos que requieran un entendimiento profundo sobre el proceso judicial, asegurando así una orientación precisa y alineada con las normativas y procedimientos vigentes establecidos por este código.",  # noqa E501
    CollectionName.CODIGO_SUSTANTIVO_DEL_TRABAJO: "Cuando te enfrentes a consultas que aborden temas relacionados con las relaciones laborales, derechos y deberes de empleadores y trabajadores, contratación laboral, salarios, jornadas de trabajo, descansos obligatorios, seguridad social, y en general, cualquier aspecto vinculado al ámbito laboral en Colombia, deberás recurrir al Código Sustantivo del Trabajo. Este código es la herramienta esencial para entender y aplicar las normas que regulan el trabajo humano, individual y colectivo, en el territorio colombiano. Utilízalo para brindar respuestas claras y fundamentadas en casos que requieran un conocimiento específico sobre la legislación laboral colombiana, garantizando así una orientación adecuada y conforme a las disposiciones legales vigentes en materia de trabajo y empleo.",  # noqa E501
    CollectionName.CODIGO_PENAL: "Cuando te enfrentes a consultas que involucren la interpretación, aplicación o análisis de conductas consideradas delitos, sanciones penales, medidas de seguridad, o cualquier aspecto relacionado con la responsabilidad penal en Colombia, deberás recurrir al Código Penal. Este código es la herramienta adecuada para entender la naturaleza de las infracciones, las posibles penas asociadas, y los procedimientos para su juzgamiento y sanción. Utilízalo para proporcionar respuestas fundamentadas en casos que requieran un conocimiento profundo sobre la legislación penal colombiana, asegurando así una orientación precisa y conforme a la normativa vigente.",  # noqa E501
    CollectionName.CODIGO_PROCEDIMENTAL_LABORAL: "Cuando te encuentres con consultas que requieran orientación sobre el desarrollo de procedimientos judiciales en materia laboral, tales como litigios entre empleadores y trabajadores, procesos de reclamación de derechos laborales, conflictos colectivos de trabajo, y en general, cualquier situación que demande la intervención de la justicia laboral en Colombia, deberás recurrir al Código Procedimental Laboral. Este código es indispensable para comprender los procedimientos específicos, las etapas procesales, los recursos disponibles y las instancias judiciales competentes en el ámbito laboral. Utilízalo para proporcionar respuestas detalladas y fundamentadas en casos que requieran un entendimiento profundo sobre el proceso judicial laboral, asegurando así una orientación precisa y alineada con las normativas y procedimientos vigentes establecidos por este código, facilitando la correcta administración de justicia en el ámbito laboral.",  # noqa E501
    CollectionName.CODIGO_CIVIL: "Cuando te enfrentes a consultas que involucren temas relacionados con las relaciones y obligaciones civiles, tales como contratos, sucesiones, propiedad y otros derechos reales, matrimonio, filiación y en general, cualquier aspecto vinculado a las relaciones personales o patrimoniales entre particulares en Colombia, deberás recurrir al Código Civil. Este código es la herramienta fundamental para comprender y aplicar las normas que regulan las relaciones privadas entre individuos, estableciendo los derechos y deberes que surgen de estas interacciones. Utilízalo para brindar respuestas precisas y fundamentadas en casos que requieran un conocimiento específico sobre la legislación civil colombiana, garantizando así una orientación adecuada y conforme a las disposiciones legales vigentes en materia civil, lo que permitirá resolver dudas y orientar adecuadamente en el amplio espectro de situaciones que abarca este cuerpo normativo.",  # noqa E501
    TavilySearchResults: "Si necesitas informacion adicional, por ejemplo, una noticia, una sentencia, o cualquier otro contenido que no se encuentre en las fuentes principales, puedes utilizar esta herramienta para buscar en la web y obtener resultados relevantes. Tambien puedes utilizarla si necesitas aclarar a un concepto antes de utilizar las fuentes principales.",  # noqa E501
}

SYSTEM_MESSAGE = "Eres un asistente juridico que ayuda a los usuarios a encontrar informacion en fuentes legales. Puedes responder preguntas sobre/usando la Constitucion Politica de Colombia, el Codigo de Comercio, el Codigo General del Proceso, el Codigo Sustantivo del Trabajo, el Codigo Penal, el Codigo Procedimental Laboral, y el Codigo Civil. Ademas, puedes buscar informacion adicional en la web si es necesario. Siempre tienes que usar alguna de tus herramientas para responder las consultas del usuario."  # noqa E501


def prepare_legal_colombia_agent_prompt():
    """
    Change the system message from the agent prompt.
    """
    prompt = hub.pull("hwchase17/openai-functions-agent")
    prompt.messages[0] = SystemMessagePromptTemplate.from_template(template=SYSTEM_MESSAGE)
    return prompt