import { CadastroFornecedorPfComponent } from './cadastro-fornecedor-pf/cadastro-fornecedor-pf.component';
import { CadastroVendedorComponent } from './cadastro-vendedor/cadastro-vendedor.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { CriarSenhaComponent } from './criar-senha/criar-senha.component';
import { CadastroProdutoComponent } from './cadastro-produto/cadastro-produto.component';
import { AuthGuard } from './guards/auth.guard';
import { CadastroFornecedorPjComponent } from './cadastro-fornecedor-pj/cadastro-fornecedor-pj.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },

{
    path: 'home',
    component: HomeComponent, canActivate: [AuthGuard]
},

{
    path: 'login',
    component: LoginComponent
},

{
  path: 'criarSenha',
  component: CriarSenhaComponent
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
  path: 'fornecedor-pj',
  component: CadastroFornecedorPjComponent, canActivate: [AuthGuard]
},
{
  path: 'fornecedor-pf',
  component: CadastroFornecedorPfComponent, canActivate: [AuthGuard]
}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
