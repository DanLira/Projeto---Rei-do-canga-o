import { Pedidos } from './../models/pedidos.model';
import { Produto } from './../models/produto.model';
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { debounceTime, map } from 'rxjs/operators';
import { fromEvent } from 'rxjs';
import { ProdutoService } from '../cadastro-produto/produto.service';
import { PedidoService } from './pedidoService.service';
import { MatDialog, MatPaginator, MatTableDataSource } from '@angular/material';
import { ModalAlertaComponent } from '../shared/component/modals/modal-alerta/modal-alerta.component';

@Component({
  selector: 'app-pedidos',
  templateUrl: './cadastro-pedidos.component.html',
  styleUrls: ['./cadastro-pedidos.component.scss']
})
export class CadastroPedidosComponent implements OnInit {

  formsPedido: FormGroup;
  pedidoList: Pedidos[] = [];
  produtoList: any[] = [];
  produtoAutocomplete: Produto[];
  idProduto: Produto;
  displayedColumns: string[] = ['idProduto', 'descProduto', 'tipoVolume', 'preco', 'qtde',  'total', 'action'];
  dataSource = new MatTableDataSource<any[]>();
  @ViewChild('MatPaginator') MatPaginator: MatPaginator;
  @ViewChild('produtoAuto') produtoAuto;

  constructor(private readonly formBuilder: FormBuilder,
              private readonly pedidoService: PedidoService,
              private readonly produtoService: ProdutoService,
              public dialog: MatDialog,
              private readonly toastr: ToastrService) { }

  ngOnInit() {
    this.createPedidoForm();

    this.produtoService.getAllProduto().subscribe((produto: Produto[]) => {
      this.produtoAutocomplete = (!!produto) ? produto : [];

      fromEvent(this.produtoAuto.nativeElement, 'keyup').pipe(
        map((event: any) => {
          return event.target.value;
        })
        , debounceTime(1000)
      ).subscribe((text: string) => {
        if (text) {
          this._filterProduto(text);
        }
    });

    });

    this.dataSource.paginator = this.MatPaginator;

  }

  private _filterProduto(paramOfFilter: string): void {
    if (!!paramOfFilter) {
      this.produtoList = this.produtoAutocomplete.filter
        (x =>
          x.descProduto.toUpperCase().includes(paramOfFilter.toUpperCase())
        );
    }
  }

  resetFiltered(): void {
    if (!this.idProduto) {

      if (this.formsPedido.get('idProduto').value !==  this.idProduto.idProduto) {

          this.formsPedido.controls['idProduto'].setValue(null);
      }
    }
  }



  createPedidoForm(): void {
    this.formsPedido = new FormGroup({
      idPedido: new FormControl(''),
      dataPedido: new FormControl(''),
      statusPedito: new FormControl(''),
      idUser: new FormControl(''),
      quantidadeProduto: new FormControl(''),
      preco: new FormControl(''),
      idProduto: new FormControl(''),
      descProduto: new FormControl(''),
      tipoVolume: new FormControl('')
    });

  }

  private adicionarProduto(): void {

    const item: any = {
      //idProduto: this.formsPedido.value.idProduto,
      descProduto: this.formsPedido.get('descProduto').value,
      preco: this.formsPedido.get('preco').value,
      tipoVolume: this.formsPedido.get('tipoVolume').value,
      quantidadeProduto: this.formsPedido.get('quantidadeProduto').value
    };

    if (this.formsPedido.get('quantidadeProduto').value === '') {
        this.toastr.warning('Favor preencher os campos obrigatorios!');
        return;
    }

    this.produtoList.push(item);
    this.dataSource.data = [...this.produtoList];
    this.formsPedido.reset();


  }



  cancelarPedido(): void {
    this.dialog.open(ModalAlertaComponent, {

   });
 }

}
