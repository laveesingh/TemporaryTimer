from django.http import HttpResponse, JsonResponse
import datetime

def home(request):
    # return HttpResponse("<h1>Hello home</h1>")
    return HttpResponse('''
    <head>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>
    </head>
    <body>
        <button id='btn'>ClickMe</button>
        <script type='text/javascript'>
        $(document).ready(function(){
            $('#btn').on('click', function(){
                console.log('button clicked')
                $.ajax({
                url: '/api',
                success: function(data, status, xhr){
                console.log(data);
                }
                })
            })
        })
        </script>
    </body>
    ''')

def api(request):
    context = {'time': datetime.datetime.now().strftime('%d/%m/%Y')}
    return JsonResponse(context)
