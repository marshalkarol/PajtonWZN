import rich
from rich import console
from rich.traceback import install
import tqdm
import time
#tqdm pozwala na wyświetlanie paska postępu, który jeszcze zwraca czasy trwania itp
#for i in tqdm.tqdm(range(10)):
#    time.sleep(1)


rich.traceback.install()

rich.get_console().clear()
rich.get_console.rule('My Awsome Script v 1.0')
rich.print('Hello :smiley: [red b]world[/red b]!')
