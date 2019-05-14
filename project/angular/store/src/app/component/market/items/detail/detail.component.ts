import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {ProviderService} from '../../../../shared/service/provider.service';
import {Comment, Item} from '../../../../shared/model/model';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss']
})
export class DetailComponent implements OnInit {

  itemId: string;
  editing = false;
  private item: Item;
  private comments: Comment[];
  private commentBody: string;

  constructor(
    private api: ProviderService,
    private router: Router,
    private route: ActivatedRoute
  ) {
  }

  ngOnInit() {
    this.itemId = this.route.snapshot.paramMap.get('id');
    this.api.get_item(Number(this.itemId)).then(item => {
      this.item = item;
    }).catch(error => console.log(error));

    this.api.get_comments(Number(this.itemId)).then(comments => {
      console.log(comments);
      this.comments = comments;
    }).catch(error => {
      console.log(error);
    });
  }

  back() {
    this.router.navigate(['']);
  }

  edit(item: Item) {
    this.editing = true;
  }

  delete(item: Item) {
    this.api.delete_item(item.id).then(resp => {
      this.back();
    }).catch(error => {
      console.log(error);
    });
  }

  putComment() {
    this.api.put_comment(Number(this.itemId), {
      description: this.commentBody
    }).then(resp => {
      this.comments.push(resp);
    }).catch(error => {
      console.log(error);
    });
  }

  clearComment() {
    this.commentBody = '';
  }

  onCancelClick() {
    this.editing = false;
  }

  onSaveClick() {
    this.api.update_item(this.item.id, this.item).then(response => {
      this.editing = false;
    }).catch(error => {
      console.log(error);
    });
  }
}
