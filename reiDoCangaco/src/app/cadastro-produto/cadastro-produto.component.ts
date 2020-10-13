import { Component, OnInit, ViewChild } from '@angular/core';
import { Produto } from '../models/produto.model';
import { FormGroup, FormBuilder } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { MatTableDataSource, MatPaginator } from '@angular/material';
import { ProdutoService } from './produto.service';

@Component({
  selector: 'app-cadastro-produto',
  templateUrl: './cadastro-produto.component.html',
  styleUrls: ['./cadastro-produto.component.scss']
})
export class CadastroProdutoComponent implements OnInit {

  produtos: Produto[];
  produtoList: Produto[] = [];
  formsRegister: FormGroup;
  filterFormProduto: FormGroup;
  displayedColumns: string[] = ['nome', 'descricao', 'quantidade', 'dataCreate', 'dateUpdate', 'action'];
  dataSource = new MatTableDataSource<Produto>();
  todoDataSource: any[];
  @ViewChild('MatPaginator') MatPaginator: MatPaginator;

  constructor(private readonly formBuilder: FormBuilder,
              private readonly produtoService: ProdutoService,
              private readonly toastr: ToastrService) { }

  ngOnInit() {
    this.formsRegister = this.formBuilder.group({
      _id: [null],
      nome: [''],
      descricao: [''],
      precoVenda: [''],
      precoCusto: [''],
      categoria: [''],
      quantidade: [''],
      createAt: [''],
      updatedAt: ['']
    });

    this.filterFormProduto = this.formBuilder.group({
      nomeFilterCtrl: [''],
      descricaoFilterCtrl: ['']
    });

    this.produtoService.getAllProduto().subscribe((produto: Produto[]) => {
      this.produtoList = (!!produto) ? produto : [];
      this.dataSource.data = [...this.produtoList];
    });
    this.dataSource.paginator = this.MatPaginator;
  }


salvarProduto() {
  const produto: Produto = {
    _id: this.formsRegister.value._id,
    nome: this.formsRegister.get('nome').value,
    descricao: this.formsRegister.get('descricao').value,
    precoVenda: this.formsRegister.get('precoVenda').value,
    precoCusto: this.formsRegister.get('precoCusto').value,
    categoria: this.formsRegister.get('categoria').value,
    quantidade: this.formsRegister.get('quantidade').value,
    updatedAt: new Date()
  };

  if (!!this.formsRegister.value._id) {
    this.produtoService.editProduto(produto).subscribe(() => {
      this.produtoService.getAllProduto().subscribe(produtos => {
        this.produtoList = produtos;
        this.dataSource.data = this.produtoList;
        this.formsRegister.reset();
        this.toastr.success('Produto atualizado com sucesso!', 'Alterar');
       });
    });

  } else {
      this.produtoService.saveProduto(produto).subscribe(() => {
       this.produtoService.getAllProduto().subscribe(produtos => {
        this.produtoList = produtos;
        this.dataSource.data = this.produtoList;
        this.formsRegister.reset();
        this.toastr.success('Produto cadastrado com sucesso!', 'Salvar');
       });
      });
    }
}

excluirProduto(id: string): void {
  this.produtoService.deleteProduto(id).subscribe(() => {
    this.produtoService.getAllProduto().subscribe(produtos => {
     this.produtoList = produtos;
     this.dataSource.data = this.produtoList;
     this.formsRegister.reset();
     this.toastr.success('Produto excluído com sucesso!', 'Excluir');
    });
   });
}

limpar() {
  this.formsRegister.reset();
  this.toastr.info('Campos limpos!', 'Limpar');
}


getRowTableProduto(value: any): void {

  this.formsRegister.get('_id').setValue(value._id);
  this.formsRegister.get('nome').setValue(value.nome);
  this.formsRegister.get('descricao').setValue(value.descricao);
  this.formsRegister.get('precoVenda').setValue(value.precoVenda);
  this.formsRegister.get('precoCusto').setValue(value.precoCusto);
  this.formsRegister.get('categoria').setValue(value.categoria);
  this.formsRegister.get('quantidade').setValue(value.quantidade);


}

}
