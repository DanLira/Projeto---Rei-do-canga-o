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
  displayedColumns: string[] = ['descProduto', 'preco', 'tipoVolume', 'dataCreate', 'dateUpdate', 'action'];
  dataSource = new MatTableDataSource<Produto>();
  @ViewChild('MatPaginator') MatPaginator: MatPaginator;

  constructor(private readonly formBuilder: FormBuilder,
              private readonly produtoService: ProdutoService,
              private readonly toastr: ToastrService) { }

  ngOnInit() {
    this.createForm();
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




  private createForm(): void {
    this.formsRegister = this.formBuilder.group({
      idProduto: [null],
      descProduto: [''],
      descAbrevProduto: [''],
      preco: [''],
      tipoVolume: [''],
      fornecedorPj: [''],
      fornecedorPf: [''],
      status: ['']
    });
  }


salvarProduto() {
  const produto: Produto = {
    idProduto: this.formsRegister.value.idProduto,
    descProduto: this.formsRegister.get('descProduto').value,
    preco: this.formsRegister.get('preco').value,
    tipoVolume: this.formsRegister.get('tipoVolume').value,
    fornecedorPj: this.formsRegister.get('fornecedorPj').value,
    fornecedorPf: this.formsRegister.get('fornecedorPf').value,

  };

  if (!!this.formsRegister.value.idProduto) {
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

  this.formsRegister.get('_id').setValue(value.idProduto);
  this.formsRegister.get('descProduto').setValue(value.descProduto);
  this.formsRegister.get('preco').setValue(value.preco);
  this.formsRegister.get('tipoVolume').setValue(value.tipoVolume);
  this.formsRegister.get('fornecedorPj').setValue(value.fornecedorPj);
  this.formsRegister.get('fornecedorPf').setValue(value.fornecedorPf);


}

}
