package objects

import (
	"reflect"
	"time"
	//"go.mongodb.org/mongo-driver/bson/primitive"
)

type Person struct {
	Name      string    `json:"name,omitempty" bson:"name,omitempty"`
	ID        string    `json:"_id,omitempty" bson:"_id,omitempty"`
	LastName  string    `json:"lastname,omitempty" bson:"lastname,omitempty"`
	Birthday  string    `json:"birthday,omitempty" bson:"birthday,omitempty"`
	BirthDate time.Time `json:"birthdate,omitempty" bson:"birthdate,omitempty"`
}

func (p *Person) GetKind() string {
	return reflect.TypeOf(p).String()
}

func (p *Person) GetID() string {
	return p.ID
}

func (p *Person) GetName() string {
	return p.Name
}

func (p *Person) SetID(s string) {
	p.ID = s
}

func (p *Person) SetName(s string) {
	p.Name = s
}
