import click

# @click.command
# def test():
#    print("Test complete")

@click.command
@click.argument('message')    # message передаётся в функцию ниже как аргумент
@click.option('--count', default=1, help='Number of messages')    # count передаётся в функцию ниже как опция (через двойной дефис) (по умолчанию единица)
def test(message, count):
   for _ in range(count):
       print(message)

if __name__ == "__main__":
   test()
