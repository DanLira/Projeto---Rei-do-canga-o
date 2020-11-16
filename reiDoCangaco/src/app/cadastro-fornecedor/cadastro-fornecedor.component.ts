import { FornecedorPf } from './../models/fornecedorPf.model';
import { ToastrService } from 'ngx-toastr';
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { MatTableDataSource, MatPaginator } from '@angular/material';
import { FornecedorPj } from '../models/fornecedorPj.model';
import { FornecedorPjService } from './service/fornecedorPj.service';
import { FornecedorPfService } from './service/fornecedorPf.service';

@Component({
  selector: 'app-cadastro-fornecedor',
  templateUrl: './cadastro-fornecedor.component.html',
  styleUrls: ['./cadastro-fornecedor.component.scss']
})
export class CadastroFornecedorComponent implements OnInit {

  fornecedorPj: FornecedorPj [];
  fornecedorPJList: FornecedorPj [] = [];
  pj: boolean;

  fornecedorPf: FornecedorPf [];
  fornecedorPfList: FornecedorPf [] = [];
  pf: boolean;

  formsRegister: FormGroup;
  filterFormFornecedorPj: FormGroup;
  filterFormFornecedorPf: FormGroup;
  displayedColumnsPj: string[] = ['razaoSocial', 'endereco', 'telefone', 'dataCreate', 'dateUpdate', 'action'];
  dataSourcePj = new MatTableDataSource<FornecedorPj>();
  displayedColumnsPf: string[] = ['nome', 'endereco', 'telefone', 'dataCreate', 'dateUpdate', 'action'];
  dataSourcePf = new MatTableDataSource<FornecedorPf>();
  todoDataSource: any[];
  @ViewChild('MatPaginator') MatPaginator: MatPaginator;

  constructor(private readonly fb: FormBuilder,
              private readonly fornecedorPjService: FornecedorPjService,
              private readonly fornecedorPfService: FornecedorPfService,
              private readonly toastr: ToastrService) { }

  ngOnInit() {
    this.createForm();
    this.createFilterFormPj();
    this.createFilterFormPf();
    this.listarFornecedorPJ();
    
    this.dataSourcePj.paginator = this.MatPaginator;

  }

  private listarFornecedorPJ(): void {
    this.fornecedorPjService.getAllFornecedorPj().subscribe((fornecedorPj: FornecedorPj[]) => {
      this.fornecedorPJList = (!!fornecedorPj) ? fornecedorPj : [];
      this.dataSourcePj.data = [...this.fornecedorPJList];
    });
  }


  private createForm(): void {
    this.formsRegister = this.fb.group({
      idFornecedorPJ: new FormControl(''),
      idFornecedorPF: new FormControl(''),
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
      estado: new FormControl(''),
      pais: new FormControl(''),
      tipoFornecedor: new FormControl(''),
      nome: new FormControl('', Validators.required),
      sexo: new FormControl(''),
      cpf: new FormControl('', Validators.required),
      flagAtivo: new FormControl(false)
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
          this.pj = true;
          this.addFormValidators(['razaoSocial', 'cnpj']);

          this.formsRegister.get('nome').clearValidators();
          this.formsRegister.get('cpf').clearValidators();
          this.formsRegister.get('nome').updateValueAndValidity();
          this.formsRegister.get('cpf').updateValueAndValidity();

      } else if (event.value === 'fornecedorPF') {
          this.pf = true;
          this.addFormValidators(['nome', 'cpf']);

          this.formsRegister.get('razaoSocial').clearValidators();
          this.formsRegister.get('cnpj').clearValidators();
          this.formsRegister.get('razaoSocial').updateValueAndValidity();
          this.formsRegister.get('cnpj').updateValueAndValidity();
      }
  }



  private salvarFornecedor(): void {

    if (this.pj) {

      const fornecedorPJ: FornecedorPj = {

        idFornecedorPJ: this.formsRegister.get('idFornecedorPJ').value,
        nomeFantasia: this.formsRegister.get('nomeFantasia').value,
        razaoSocial: this.formsRegister.get('razaoSocial').value,
        cnpj: this.formsRegister.get('cnpj').value,
        nickName: this.formsRegister.get('nickName').value,
        telefone: this.formsRegister.get('telefone').value,
        celular: this.formsRegister.get('celular').value,
        email: this.formsRegister.get('email').value,
        endereco: this.formsRegister.get('endereco').value,
        complemento: this.formsRegister.get('complemento').value,
        bairro: this.formsRegister.get('bairro').value,
        cep: this.formsRegister.get('cep').value,
        cidade: this.formsRegister.get('cidade').value,
        pais: this.formsRegister.get('pais').value,
        estado: this.formsRegister.get('estado').value,
        status: this.formsRegister.get('flagAtivo').value ? 'I' : 'A',

      };
      if (this.formsRegister.value.idFornecedorPJ) {

          this.fornecedorPjService.editFornecedorPj(fornecedorPJ).subscribe(() => {
            this.listarFornecedorPJ();
            this.toastr.success('Fornecedo editado com sucesso!', 'Editar');
            this.limpar();
          });
      } else {
         this.fornecedorPjService.saveFornecedorPj(fornecedorPJ).subscribe(() => {
          this.listarFornecedorPJ();
          this.toastr.success('Fornecedor salvo com sucesso!', 'Salvar');
          this.limpar();
          });
      }

    } else {

    }

  }


  private limpar(): void {
    this.formsRegister.reset();
    this.toastr.info('Campos limpos!', 'Limpar');
  }


}
