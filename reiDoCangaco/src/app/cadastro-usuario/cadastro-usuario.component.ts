import { Component, Inject, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { MatTableDataSource, MAT_DIALOG_DATA, MatDialogRef, MatPaginator } from '@angular/material';
import { ToastrService } from 'ngx-toastr';
import { SubSink } from 'subsink/dist/subsink';
import { Usuarios } from '../models/usuarios.model';
import { UsuarioService } from './usuario.service';

@Component({
  selector: 'app-cadastro-usuario',
  templateUrl: './cadastro-usuario.component.html',
  styleUrls: ['./cadastro-usuario.component.scss']
})
export class CadastroUsuarioComponent implements OnInit {

  usuarioEdit: Usuarios[] = [];
  formsRegister: FormGroup;
  filterFormNutricionista: FormGroup;
  usuarioList: Usuarios[] = [];
  filterFormUsuario: FormGroup;
  displayedColumns: string[] = ['login', 'dateUpdate', 'action'];
  dataSource = new MatTableDataSource<Usuarios>();
  todoDataSource: any[];
  @ViewChild('MatPaginator') MatPaginator: MatPaginator;

  private readonly subs = new SubSink();

  constructor( private readonly formBuilder: FormBuilder,
               private readonly usuarioService: UsuarioService,
               private readonly toastr: ToastrService) { }

  ngOnInit() {
    this.dataSource.paginator = this.MatPaginator;
    this.createForm();

    this.filterFormUsuario = this.formBuilder.group({
      nomeFilterCtrl: ['']
    });

    this.usuarioService.getAllUsuario().subscribe((usuario: Usuarios[]) => {
      this.usuarioList = (!!usuario) ? usuario : [];
      this.dataSource.data = [...this.usuarioList];
    });

  }

  private createForm(): void {
    this.formsRegister = new FormGroup({

        _id: new FormControl(null),
        login: new FormControl('', Validators.required),
        senha: new FormControl('', Validators.required),
        createAt: new FormControl(''),
        updatedAt: new FormControl(''),
        //ativo: new FormControl(this.data.usuario.ativo, false)
     });
  }


  saveUsuario(): void {
    const usuario: Usuarios = {
      _id: this.formsRegister.get('_id').value,
      login: this.formsRegister.get('login').value,
      senha: this.formsRegister.get('senha').value,
      //ativo: !this.formsRegister.get('ativo').value,
      updatedAt: new Date()

    };
    if (this.formsRegister.value._id) {
        this.usuarioService.editUsuario(usuario, this.formsRegister.value._id).subscribe(() => {
          this.usuarioService.getAllUsuario().subscribe(usuarios => {
            this.usuarioList = (!!usuarios) ? usuarios : [];
            this.dataSource.data = [...this.usuarioList];
            this.toastr.success('Usuário editado com sucesso!', 'Editar');

          });
        });
    } else {
      this.subs.sink =  this.usuarioService.saveUsuario(usuario).subscribe(() => {
          this.usuarioService.getAllUsuario().subscribe(usuarios => {
            this.usuarioList = (!!usuarios) ? usuarios : [];
            this.dataSource.data = [...this.usuarioList];
            this.toastr.success('Usuário salvo com sucesso!', 'Salvar');

          });
        });
    }
  }

  private limpar(): void {
    this.formsRegister.reset();
    this.toastr.info('Campos limpos com sucesso!');
  }


  excluirUsuario(id: string): void {
    this.usuarioService.deleteUsuario(id).subscribe(() => {
      this.usuarioService.getAllUsuario().subscribe(usuarios => {
       this.usuarioList = usuarios;
       this.dataSource.data = this.usuarioList;
       this.filterFormUsuario.reset();
       this.toastr.success('Usuário excluído com sucesso!', 'Excluir');
      });
     });
  }


  filterTabelaUsuario(): void {
    let filteredTable: Usuarios[] = this.usuarioList;
    if (!this.filterFormUsuario.value.nomeFilterCtrl) {
      this.dataSource.data = [...this.usuarioList];
    }
    if (this.filterFormUsuario.value.nomeFilterCtrl) {
      filteredTable = filteredTable.filter
      ( x => {
        return x.login ? x.login.toUpperCase().includes(this.filterFormUsuario.value.nomeFilterCtrl.toUpperCase()) : null;
      });
     }
    this.dataSource.data = filteredTable;
  }

}
