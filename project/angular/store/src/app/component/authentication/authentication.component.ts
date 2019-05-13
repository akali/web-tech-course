import {Component, OnInit} from '@angular/core';
import {AuthService} from '../../shared/service/auth.service';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-authentication',
  templateUrl: './authentication.component.html',
  styleUrls: ['./authentication.component.scss']
})
export class AuthenticationComponent implements OnInit {

  authenticated = false;
  username = '';
  password = '';
  errors: string = null;

  constructor(
    private auth: AuthService,
    private route: ActivatedRoute,
    private router: Router
  ) {
  }

  ngOnInit() {
    this.authenticated = this.auth.authenticated();
  }

  authenticate(username: string, password: string) {
    this.auth.authenticate(username, password).then(res => {
      this.authenticated = true;
      this.router.navigateByUrl('/');
    }).catch(err => {
      this.errors = err;
    });
  }
}
