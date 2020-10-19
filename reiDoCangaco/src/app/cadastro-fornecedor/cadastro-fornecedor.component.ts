import { FornecedorPf } from './../models/fornecedorPf.model';
import { ToastrService } from 'ngx-toastr';
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { MatTableDataSource, MatPaginator } from '@angular/material';
import { FornecedorPj } from '../models/fornecedorPj.model';

@Component({
  selector: 'app-cadastro-fornecedor',
  templateUrl: './cadastro-fornecedor.component.html',
  styleUrls: ['./cadastro-fornecedor.component.scss']
})
export class CadastroFornecedorComponent implements OnInit {

  fornecedorPj: FornecedorPj [];
  fornecedorPJList: FornecedorPj [] = [];

  fornecedorPf: FornecedorPf [];
  fornecedorPfList: FornecedorPf [] = [];

  formsRegister: FormGroup;
  filterFormFornecedorPj: FormGroup;
  filterFormFornecedorPf: FormGroup;
  displayedColumnsPj: string[] = ['razaoSocial', 'endereco', 'telefone', 'dataCreate', 'dateUpdate', 'action'];
  dataSourcePj = new MatTableDataSource<FornecedorPj>();
  displayedColumnsPf: string[] = ['nome', 'endereco', 'telefone', 'dataCreate', 'dateUpdate', 'action'];
  dataSourcePf = new MatTableDataSource<FornecedorPf>();
  todoDataSource: any[];
  @ViewChild('MatPaginator') MatPaginator: MatPaginator;

  constructor(private readonly fb: FormBuilder, private readonly toastr: ToastrService) { }

  ngOnInit() {
    this.createForm();
    this.createFilterFormPj();
    this.createFilterFormPf();
    this.dataSourcePj.paginator = this.MatPaginator;

  }


  private createForm(): void {
    this.formsRegister = this.fb.group({
      id: new FormControl(''),
      razaoSocial: new FormControl('', Validators.required),
      nomeFantasia: new FormControl(''),
      nickName: new FormControl(''),
      cnpj: new FormControl('', Validators.required),
      telefone: new FormControl('', Validators.required),
      celular: new FormControl('', Validators.required),
      email: new FormControl(''),
      endereco: new FormControl('', Validators.required),
      complemento: new FormControl(''),
      bairro: new FormControl(''),
      cep: new FormControl('', Validators.required),
      cidade: new FormControl(''),
      uf: new FormControl(''),
      pais: new FormControl(''),
      tipoFornecedor: new FormControl(''),
      nome: new FormControl('', Validators.required),
      sexo: new FormControl(''),
      cpf: new FormControl('', Validators.required)
    });
  }



  private createFilterFormPj(): void {
    this.filterFormFornecedorPj = this.fb.group({
      razaoSocialFilterCtrl: new FormControl('')
    });
  }
  private createFilterFormPf(): void {
    this.filterFormFornecedorPf = this.fb.group({
      nomeFilterCtrl: new FormControl('')
    });
  }

  private addFormValidators(listaCampos = []): void {
    listaCampos.forEach(campo => {
        this.formsRegister.get(campo).setValidators([Validators.required]);
    });
  }

  private fornecedorSelecionado(event: any): void {

    if (event.value === 'fornecedorPJ') {
          this.addFormValidators(['razaoSocial', 'cnpj']);

          this.formsRegister.get('nome').clearValidators();
          this.formsRegister.get('cpf').clearValidators();
          this.formsRegister.get('nome').updateValueAndValidity();
          this.formsRegister.get('cpf').updateValueAndValidity();

      } else if (event.value === 'fornecedorPF') {
          this.addFormValidators(['nome', 'cpf']);

          this.formsRegister.get('razaoSocial').clearValidators();
          this.formsRegister.get('cnpj').clearValidators();
          this.formsRegister.get('razaoSocial').updateValueAndValidity();
          this.formsRegister.get('cnpj').updateValueAndValidity();
      }
  }


  private limpar(): void {
    this.formsRegister.reset();
    this.toastr.info('Campos limpos!', 'Limpar');
  }


}
