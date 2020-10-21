import { CadastroVendedorComponent } from './cadastro-vendedor/cadastro-vendedor.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { CriarSenhaComponent } from './criar-senha/criar-senha.component';
import { CadastroProdutoComponent } from './cadastro-produto/cadastro-produto.component';
import { AuthGuard } from './guards/auth.guard';
import { CadastroFornecedorComponent } from './cadastro-fornecedor/cadastro-fornecedor.component';
import { CadastroUsuarioComponent } from './cadastro-usuario/cadastro-usuario.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },

{
    path: 'home',
    component: HomeComponent,
    // canActivate: [AuthGuard]
},

{
    path: 'login',
    component: LoginComponent
},

{
  path: 'usuario',
  component: CadastroUsuarioComponent
},
{
  path: 'produto',
  component: CadastroProdutoComponent,
  //canActivate: [AuthGuard]
},
{
  path: 'vendedor',
  component: CadastroVendedorComponent, canActivate: [AuthGuard]
},
{
  path: 'fornecedor',
  component: CadastroFornecedorComponent, 
  //canActivate: [AuthGuard]
},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
