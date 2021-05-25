import execjs
from loguru import logger

logger.info(execjs.get().name)  # 查看调用的环境

ctx = execjs.compile("""function add(x, y){
return x + y;
}
""")

logger.info(f'result:{ctx.call("add", 1, 2)}')
