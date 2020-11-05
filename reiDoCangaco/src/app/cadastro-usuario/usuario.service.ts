import { Usuarios } from './../models/usuarios.model';
import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  readonly apiUrl = 'http://localhost:5000';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
 constructor(private readonly _HTTP: HttpClient) { }


   getAllUsuario(): Observable<Usuarios[]> {
      //  return this._HTTP.get<Usuarios[]>(this.apiUrl + 'user/getAll', {});
       return this._HTTP.get<Usuarios[]>(this.apiUrl + '/users', {});
   }
   getUsuarioById(idUsuarios: string): Observable<any> {
       return this._HTTP.get(this.apiUrl + '/Usuarios/?id=' + idUsuarios);
   }
   saveUsuario(usuario: Usuarios): Observable<Usuarios> {
       return this._HTTP.post<Usuarios>(this.apiUrl + 'user/create', usuario, this.httpOptions);
   }
   editUsuario(usuario: Usuarios): Observable<any> {

     return this._HTTP.put(this.apiUrl + 'update/?id=' + usuario.id, usuario, this.httpOptions);
   }
   deleteUsuario(id: string): Observable<any> {
       return this._HTTP.delete(this.apiUrl + 'delete/' + id, this.httpOptions);
   }

}
