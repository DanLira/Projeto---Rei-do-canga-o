import { Usuarios } from './../models/usuarios.model';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../guards/auth.service';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { UsuarioService } from '../cadastro-usuario/usuario.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  returnUrl: string;
  usuariosList: Usuarios[];
  userInfo: Usuarios[];
  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router,
    private readonly toastr: ToastrService,
    private readonly usuarioService: UsuarioService
  ) {}

  ngOnInit() {
    this.loginForm = this.fb.group({
      login: ['', Validators.required],
      senha: ['', Validators.required]
    });
    this.returnUrl = '/home';
    this.authService.logout();
  //   this.usuarioService.getAllUsuario()
  //   .subscribe((usuarios: Usuarios[]) => {
  //     this.usuariosList = (!!usuarios) ? usuarios : [];
  // });
  }

  get f() { return this.loginForm.controls; }

  fazerLogin() {
  if (this.loginForm.invalid) {
    return;
 } else {
   const user = this.usuariosList.find(x => x.login === this.f.login.value
    && x.senha === this.f.senha.value );
   if (user) {
       console.log('Login successful');
       sessionStorage.setItem('isLoggedIn', 'true');
       sessionStorage.setItem('token', this.f.login.value);
       sessionStorage.setItem('key', user._id);
       this.userInfo = JSON.parse(sessionStorage.getItem('userInfo'));
       this.router.navigate([this.returnUrl]);
    } else {
      this.toastr.warning('Login ou Senha invalida!', '');
    }
  }
}

}
