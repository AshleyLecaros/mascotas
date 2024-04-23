from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def perro(request):
    return HttpResponse(
        """ <h1> Perro Labrador </h1> <p> Los perros labradores son una de las razas más populares del mundo debido a su amabilidad, inteligencia y lealtad. </p> <img src="https://media.istockphoto.com/id/1069531070/es/foto/grupos-de-perros-cachorros-de-labrador-perro-perdiguero-de-labrador-cachorro-chocolate-delante.jpg?s=1024x1024&w=is&k=20&c=df4bcJqeMOzpDMn43RxwKZcgEbt8QRnUbrfQMwkhZ-0=" alt="Texto alternativo" width= "ancho" height= "alto"/> """
        )
    
def about(request):
    return HttpResponse(
        "vista about"
    )
    
def contact(request): 
    return HttpResponse(
        """
        <h1>Vista para el Contacto</h1> 
        <form action="/contacto" method="">
            <input type="text" name="nombre"
            placeholder="Nombre">
            <input type="email" name="correo"
            placeholder="Correo electrónico">
            <textarea name="mensaje"
            placeholder="Mensaje"></textarea>
            <input type="submit" values="Enviar">
        </form> """
    )
    
def home(request):
    return HttpResponse(
        """ 
        <h1>Ejemplo de aplicación web con múltiples 
        vistas!!!</h1>
        <p>Esta es mi primera aplicación con Django
        mostrando HTML</p>
        <img src="https://picsum.photos/200/300" />
        """
    )