import { SharedModule } from './shared/shared.module';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { LoginComponent } from './login/login.component';
import { ToastrModule } from 'ngx-toastr';
import { CadastroClienteComponent } from './cadastro-cliente/cadastro-cliente.component';
import { CadastroProdutoComponent } from './cadastro-produto/cadastro-produto.component';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatTableModule } from '@angular/material/table';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatMenuModule } from '@angular/material/menu';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatSelectModule, MatDialogModule } from '@angular/material';
import { MatGridListModule } from '@angular/material/grid-list';
import { LayoutModule } from '@angular/cdk/layout';
import { CriarSenhaComponent } from './criar-senha/criar-senha.component';
import { AuthService } from './guards/auth.service';
import { AuthGuard } from './guards/auth.guard';
import { CadastroUsuarioComponent } from './cadastro-usuario/cadastro-usuario.component';
import { CadastroVendedorComponent } from './cadastro-vendedor/cadastro-vendedor.component';
import { CadastroPedidosComponent } from './cadastro-pedidos/cadastro-pedidos.component';
import { LogComponent } from './log/log.component';
import { RelatorioVendasComponent } from './relatorio-vendas/relatorio-vendas.component';
import { CadastroFornecedorComponent } from './cadastro-fornecedor/cadastro-fornecedor.component';

@NgModule({
  declarations: [	
    AppComponent,
    HomeComponent,
    LoginComponent,
    CadastroClienteComponent,
    CadastroProdutoComponent,
    CadastroPedidosComponent,
    CriarSenhaComponent,
    CadastroUsuarioComponent,
    CadastroVendedorComponent,
    LogComponent,
    RelatorioVendasComponent,
      CadastroFornecedorComponent
   ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatCardModule,
    MatInputModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
    MatToolbarModule,
    ToastrModule,
    MatPaginatorModule,
    MatTableModule,
    MatExpansionModule,
    MatMenuModule,
    MatFormFieldModule,
    FormsModule,
    MatSelectModule,
    ReactiveFormsModule,
    ToastrModule.forRoot(),
    MatGridListModule,
    LayoutModule,
    SharedModule,
    MatDialogModule

  ],
  providers: [AuthGuard, AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
