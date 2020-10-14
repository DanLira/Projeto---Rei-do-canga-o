import { ToastrService } from 'ngx-toastr';
import { FornecedorPj } from './../models/fornecedor.model';
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { MatTableDataSource, MatPaginator } from '@angular/material';

@Component({
  selector: 'app-cadastro-fornecedor',
  templateUrl: './cadastro-fornecedor.component.html',
  styleUrls: ['./cadastro-fornecedor.component.scss']
})
export class CadastroFornecedorComponent implements OnInit {

  formsRegister: FormGroup;
  filterFormFornecedor: FormGroup;
  displayedColumns: string[] = ['nome', 'descricao', 'quantidade', 'dataCreate', 'dateUpdate', 'action'];
  dataSource = new MatTableDataSource<FornecedorPj>();
  todoDataSource: any[];
  @ViewChild('MatPaginator') MatPaginator: MatPaginator;

  constructor(private readonly fb: FormBuilder, private readonly toastr: ToastrService) { }

  ngOnInit() {
    this.createForm();
    this.createFilterForm();
    this.dataSource.paginator = this.MatPaginator;
  }


  private createForm(): void {
    this.formsRegister = this.fb.group({
      id: new FormControl(''),
      razaoSocial: new FormControl('', Validators.required),
      nomeFantasia: new FormControl(''),
      nickName: new FormControl(''),
      cnpj: new FormControl('', Validators.required),
      telefone: new FormControl(''),
      celular: new FormControl(''),
      email: new FormControl('', Validators.required),
      endereco: new FormControl('', Validators.required)
    });
  }

  private createFilterForm(): void {
    this.filterFormFornecedor = this.fb.group({
      razaoSocialFilterCtrl: new FormControl(''),
      nomeFantasiaFilterCtrl: new FormControl('')
    });
  }



}
