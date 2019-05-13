import {Component, OnInit} from '@angular/core';
import {AuthService} from './shared/service/auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'store';
  private authenticated = false;

  constructor(
    private auth: AuthService,
    private router: Router) {
  }

  ngOnInit(): void {
    this.authenticated = this.auth.authenticated();
  }

  onPostItemClick() {
    this.router.navigate(['/post-item']);
  }

  logout() {
    localStorage.clear();
    this.authenticated = false;
  }

  onLoginClick() {
    this.router.navigate(['/login']);
  }
}
