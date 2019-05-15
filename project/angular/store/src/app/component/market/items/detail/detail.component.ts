import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {ProviderService} from '../../../../shared/service/provider.service';
import {Category, Comment, Item} from '../../../../shared/model/model';
import {AuthService} from '../../../../shared/service/auth.service';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss']
})
export class DetailComponent implements OnInit {

  itemId: string;
  editing = false;
  categories: Category[];
  currentCategory: Category;
  private item: Item;
  private comments: Comment[];
  private commentBody: string;

  constructor(
    private api: ProviderService,
    private router: Router,
    private route: ActivatedRoute,
    private authenticationService: AuthService
  ) {
  }

  ngOnInit() {

    this.itemId = this.route.snapshot.paramMap.get('id');
    this.api.get_item(Number(this.itemId)).then(item => {
      console.log(item);
      this.item = item;
      this.fetchCategories();
    }).catch(error => console.log(error));
    this.fetchComments();
  }

  fetchCategories() {
    this.api.get_categories().then(categories => {
      console.log(categories);
      this.categories = categories;
      this.currentCategory = this.categories.filter(category => {
        return category.id === this.item.category_id;
      })[0];
    }).catch(err => {
      console.error(err);
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
      this.fetchComments();
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
    this.item.category_id = this.currentCategory.id;
    console.log(this.currentCategory);
    this.api.update_item(this.item.id, this.item).then(response => {
      this.editing = false;
    }).catch(error => {
      console.log(error);
    });
  }

  onSelectChange($event: Event) {
    console.log($event);
  }

  private fetchComments() {
    this.api.get_comments(Number(this.itemId)).then(comments => {
      console.log(comments);
      this.comments = null;
      setTimeout(() => {
        this.comments = comments;
      }, 200);
    }).catch(error => {
      console.log(error);
    });
  }

  isAuthenticated() {
    return this.authenticationService.authenticated();
  }
}
