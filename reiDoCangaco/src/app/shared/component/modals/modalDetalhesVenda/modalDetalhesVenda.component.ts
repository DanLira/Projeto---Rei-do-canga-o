import { PedidoProduto } from './../../../../models/pedido-produto.model';
import { Component, Inject, OnInit, ViewChild } from '@angular/core';
import { MatDialogRef, MatPaginator, MatTableDataSource, MAT_DIALOG_DATA } from '@angular/material';
import { Pedidos } from 'src/app/models/pedidos.model';

@Component({
  selector: 'app-modalDetalhesVenda',
  templateUrl: './modalDetalhesVenda.component.html',
  styleUrls: ['./modalDetalhesVenda.component.scss']
})
export class ModalDetalhesVendaComponent implements OnInit {

  dataSource = new MatTableDataSource<Pedidos>();
  @ViewChild(MatPaginator) MatPaginator: MatPaginator;
  displayedColumns: string[] = ['descProduto', 'tipoVolume'];
  rows: Pedidos[] = [];
  constructor(@Inject(MAT_DIALOG_DATA) public data: any,
              public dialogRef: MatDialogRef<ModalDetalhesVendaComponent>) { }

  ngOnInit() {
    this.rows = this.data.detalhes;
    this.dataSource.data = this.rows;
    this.dataSource.paginator = this.MatPaginator;

  }

  closeDialog(): void {
    this.dialogRef.close(false);
  }

}
